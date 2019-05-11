import uuid
import os


def make_real_uuids():
    party_uuid_list = []
    for i in range(96):
        party_uuid = uuid.uuid4()
        uuid_string = str(party_uuid)
        party_uuid_list.append(uuid_string)

    UUID_FILE = os.path.join('uuids.txt')
    with open(UUID_FILE, mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(str(line) for line in party_uuid_list))


def make_test_uuids():
    party_uuid_list = []
    for i in range(5):
        party_uuid = uuid.uuid4()
        uuid_string = str(party_uuid)
        party_uuid_list.append(uuid_string)

    UUID_FILE = os.path.join('test_uuids.txt')
    with open(UUID_FILE, mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(str(line) for line in party_uuid_list))
