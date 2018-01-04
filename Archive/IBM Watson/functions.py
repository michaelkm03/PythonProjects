from watson_developer_cloud import NaturalLanguageClassifierV1
import json

# Creds
username ='d47e096c-6d4d-4632-ab9e-5bcf321b02c4'
password = 'DNFAAYh7WLNu'

natural_language_classifier = NaturalLanguageClassifierV1(
    username=username,
    password=password)

classifiers = natural_language_classifier.list()
# print(json.dumps(classifiers, indent=2))