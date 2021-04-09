from Stella import StellaDB

reports = StellaDB.reports

def reports_db(chat_id: int, report_arg: bool):
    report_data = reports.find_one(
        {
            'chat_id': chat_id
        }
    )
    if report_data is None:
        _id = reports.count_documents({}) + 1
        reports.insert_one(
            {
                '_id': _id,
                'chat_id': chat_id,
                'reports': report_arg
            }
        )
    else:
        reports.update(
                {
                    'chat_id': chat_id
                },
                {
                    '$set': {
                        'reports': report_arg
                    }
                },
                upsert=True
            )

def get_report(chat_id: int) -> bool:
    report_data = reports.find_one(
        {
            'chat_id': chat_id
        }
    )
    if report_data is not None:
        return report_data['reports']
    else:
        return True