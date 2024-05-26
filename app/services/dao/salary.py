from datetime import timedelta
from typing import List, Optional

import pytz
from aiogram import types
from bson import ObjectId
from pymongo import ASCENDING

from app.services.dao.base import DAO
from app.models import InputData


class SalaryDAO(DAO):
    async def aggregate(self, input_data: InputData):
        date_formats = {
            "hour": ("%Y-%m-%dT%H:00:00", timedelta(hours=1)),
            "day": ("%Y-%m-%dT00:00:00", timedelta(days=1)),
            "month": ("%Y-%m-01T00:00:00", timedelta(days=30))
        }

        dt_format, delta = date_formats[input_data.group_type]

        pipeline = [
            {
                "$match": {
                    "dt": {"$gte": input_data.dt_from, "$lte": input_data.dt_upto}
                }
            },
            {
                "$group": {
                    "_id": {
                        "$dateToString": {
                            "format": dt_format,
                            "date": "$dt",
                            "timezone": "UTC"
                        }
                    },
                    "total_value": {"$sum": "$value"}
                }
            },
            {
                "$sort": {"_id": 1}
            }
        ]

        results = await self.collection.aggregate(pipeline).to_list(length=None)
        expected_intervals = self._generate_expected_intervals(input_data, dt_format, delta)

        # Prepare a dictionary of results for easy lookup
        results_dict = {item["_id"]: item["total_value"] for item in results}

        # Prepare the output, ensuring every expected interval is represented
        dataset = [results_dict.get(interval, 0) for interval in expected_intervals]
        labels = expected_intervals

        result = {
            "dataset": dataset,
            "labels": labels
        }
        
        return result

    @staticmethod
    def _generate_expected_intervals(input_data: InputData, dt_format: str, delta: timedelta):
        # Generate all expected intervals within the date range
        current = input_data.dt_from.replace(tzinfo=pytz.UTC)
        dt_upto = input_data.dt_upto.replace(tzinfo=pytz.UTC)
        expected_intervals = []

        while current <= dt_upto:
            expected_intervals.append(current.strftime(dt_format))
            if input_data.group_type == 'month':
                # Handle month increments correctly
                if current.month == 12:
                    current = current.replace(year=current.year + 1, month=1)
                else:
                    current = current.replace(month=current.month + 1)
            else:
                current += delta

        return expected_intervals
