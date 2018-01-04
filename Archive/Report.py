from xml.dom import minidom

xmldoc = minidom.parse('report-failed.xml')
items = xmldoc.getElementsByTagName('testcase')
failed = xmldoc.getElementsByTagName('failure')

status_of_apps = {}

print ''
print '############### SUCCESSFULLY UPLOADED TO ITUNES CONNECT ####################'
print ''

# Finds alias (build name of app)
for i in items:
    app_alias = items[5].attributes['name'].value.split(' ')[5]

for j in failed:
    stktrace = failed[0].attributes['message'].value
    error = stktrace.split("`<main>'")

print app_alias
print status_of_apps
print error