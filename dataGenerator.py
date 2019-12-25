from faker import Faker
import datetime
import random
import json
fake = Faker()
print(fake)

# def datetime_handler(x):
#     if isinstance(x, datetime.date):
#         return x.isoformat()
#     raise TypeError("Unknown type")

data = {
    "user_id": 1,
    "warehouse": {
        "inbox": 
            [
                {
                    "title": "Go to the dinner with Annel",
                    "date": "11.01.2019"
                }
            ],
        "projects": []
    },
    "smart_lists":
        {
            "delegated": [],
            "next_actions": [],
            "meetings": []
        },
    "unactionable":
        {
            "someday": [],
            "references": []
        }
}

def generate_actions(n = 6, project = False):
    n = random.randint(1,n)
    data = []
    for i in range(n):
        entry = {}
        entry['title'] = fake.sentence(nb_words=7, variable_nb_words=True, ext_word_list=None)
        entry['created_date'] = fake.past_date(start_date="-30d", tzinfo=None).isoformat()
        entry['deadline'] = fake.future_date(end_date="+30d", tzinfo=None).isoformat()
        entry['place'] = fake.address()
        entry['info'] = fake.text()

        if project:
            entry['actions'] = []
            k = random.randint(1,5)
            entry['actions'] = generate_actions(k)
        
        data.append(entry)
    print(f'\n\n.{data}.\n\n')
    return data

data = []
for i in range(500):
    entry = {}
    entry['user_id'] = i
    entry['warehouse'] = {}
    entry['warehouse']['inbox'] = []
    entry['warehouse']['projects'] = []

    entry['smart_lists'] = {}
    entry['smart_lists']['delegated'] = []
    entry['smart_lists']['next_actions'] = []
    entry['smart_lists']['meetings'] = []

    entry['unactionable'] = {}
    entry['unactionable']['someday'] = []
    entry['unactionable']['references'] = []
    
    # populate
    entry['warehouse']['inbox'] = generate_actions()
    entry['warehouse']['projects'] = generate_actions(project = True)
    entry['smart_lists']['delegated'] = generate_actions()
    entry['smart_lists']['next_actions'] = generate_actions()
    entry['smart_lists']['meetings'] = generate_actions()
    entry['unactionable']['someday'] = generate_actions()
    entry['unactionable']['references'].append({'name': fake.love(), 'info': fake.texts(), 'source': fake.url()})
    data.append(entry)

data = json.dumps(data)
with open('gtd.json', 'w') as file:
    file.write(data)