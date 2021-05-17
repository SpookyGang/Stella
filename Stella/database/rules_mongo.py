from Stella import StellaDB

rules = StellaDB.rules 

def set_rules_db(chat_id, chat_rules):
    rule_data = rules.find_one(
        {
            'chat_id': chat_id
        }
    )

    _id = rules.count_documents({}) + 1 
    if rule_data is None:
        rules.insert_one(
            {
                '_id': _id,
                'chat_id': chat_id,
                'rules': chat_rules,
                'private_note': True,
                'button_text': 'Rules'
            }
        )
    else:
        rules.update_one(
            {
                'chat_id': chat_id
            },
            {
                '$set': {
                    'rules': chat_rules
                }
            },
            upsert=True
        )

def get_rules(chat_id: int):
    rule_data = rules.find_one(
        {
            'chat_id': chat_id
        }
    )

    if rule_data is not None:
        rules_text = rule_data['rules']
        return rules_text
    else:
        return None

def set_private_rule(chat_id, private_note):
    rule_data = rules.find_one(
        {
            'chat_id': chat_id
        }
    )

    _id = rules.count_documents({}) + 1 
    if rule_data is None:
        rules.insert_one(
            {
                '_id': _id,
                'chat_id': chat_id,
                'rules': None,
                'private_note': private_note,
                'button_text': 'Rules'
            }
        )
    else:
        rules.update_one(
            {
                'chat_id': chat_id
            },
            {
                '$set': {
                    'private_note': private_note
                }
            }
        )

def get_private_note(chat_id) -> bool:
    rule_data = rules.find_one(
        {
            'chat_id': chat_id
        }
    )

    if rule_data is not None:
        return rule_data['private_note']
    else:
        return True

def set_rule_button(chat_id, rule_button):
    rule_data = rules.find_one(
        {
            'chat_id': chat_id
        }
    )

    _id = rules.count_documents({}) + 1 
    if rule_data is None:
        rules.insert_one(
            {
                '_id': _id,
                'chat_id': chat_id,
                'rules': None,
                'private_note': None,
                'button_text': rule_button
            }
        )
    else:
        rules.update_one(
            {
                'chat_id': chat_id
            },
            {
                '$set': {
                    'button_text': rule_button
                }
            }
        )

def get_rules_button(chat_id):
    rule_data = rules.find_one(
        {
            'chat_id': chat_id
        }
    )
    if rule_data is not None:
        return rule_data['button_text']
    else:
        return 'Rules'

