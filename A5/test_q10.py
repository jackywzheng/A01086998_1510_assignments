from unittest import TestCase
from A5.q10 import database_shared_headings


class TestDatabase_shared_headings(TestCase):
    def test_valid_database(self):
        data1 = {'jgoodall': {'surname': 'Goodall', 'name': 'Jane', 'born': 1934, 'died': None,
                              'notes': 'Primate research', 'author': ['In the Shadow of Man', 'The Chimps of Gombe']
                              },
                 'rfranklin': {'surname': 'Franklin', 'name': 'Rosalind', 'born': 1920, 'died': 1957,
                               'notes': 'DNA research'
                               },
                 'aturing': {'surname': 'Turing', 'name': 'Alan', 'born': 1912, 'died': 1954, 'notes': 'polymath',
                             'author': ['Systems of Logic based on Ordinals’]']
                             }
                 }
        self.assertEqual(database_shared_headings(data1), {'name', 'surname', 'died', 'born', 'notes'})

    def test_no_same_key_(self):
        sample = {'jgoodall': {'surname': 'Goodall', 'name': 'Jane', 'born': 1934, 'died': None,
                               'notes': 'Primate research', 'author': ['In the Shadow of Man', 'The Chimps of Gombe']
                               },
                 'rfranklin-': {'sur-name': 'Franklin', 'name-': 'Rosalind', 'born-': 1920, 'died-': 1957,
                                'notes': 'DNA research'
                                },
                 'aturing_': {'sur_name': 'Turing', 'name_': 'Alan', 'born_': 1912, 'died_': 1954, 'notes_': 'polymath',
                              'author': ['Systems of Logic based on Ordinals’]']
                              }
                  }
        self.assertEqual(database_shared_headings(sample), set())
