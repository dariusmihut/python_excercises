TELEGRAM_TEMPLATE = "{0}{2}{1}   fdsfsdfsdfsdf "
TELEGRAM_LENGTH = 30
ID_LENGTH = 4
ACTION_LENGTH = 10
DESCRIPTION_LENGTH = 16

id = "4832"
action = "copy"
description = "test description over over over"

composed_telegram = TELEGRAM_TEMPLATE.format(
    id.ljust(ID_LENGTH," ")[:ID_LENGTH],
    action.ljust(ACTION_LENGTH," ")[:ACTION_LENGTH],
    description.ljust(DESCRIPTION_LENGTH," ")[:DESCRIPTION_LENGTH]
    )[:TELEGRAM_LENGTH]

print(composed_telegram)