content = "hello world"
name = "marc"

print "way 1"
print content + " " + name
print "way 2"
print "%s %s" % (content, name)
print "way 3"
print "{0} {0}".format(content, name)