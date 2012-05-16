# -*- coding: utf-8 -*-
"""Recipe insertinto"""
import os


class Recipe(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options

    def install(self):
        """
        client1 = ${client1:location}/etc/zope.conf insert-before "</zeoclient>" "\n\tread-only true\n"
        """
        options = self.options.copy()
        del options['recipe']

        for key, option in options.items():
            filename, insert_type = option.split(' ')[:2]
            _, pivot, _, insert_text, _ = option.split('"')

            if not os.path.exists(filename):
                raise Exception("You must provide a real filename.")

            insert_text = insert_text.replace('\\n', '\n').replace('\\t', '\t')
            filecontents = open(filename).read()

            if insert_text in filecontents:
                return

            insert_location = filecontents.find(pivot)

            if insert_location > -1:
                if insert_type == "insert-before":
                    filecontents = "%s%s%s" % (
                        filecontents[:insert_location - 1],
                        insert_text,
                        filecontents[insert_location - 1:])
                elif insert_type == "insert-after":
                    filecontents = "%s%s%s" % (
                        filecontents[:(insert_location - 1) + len(pivot)],
                        insert_text,
                        filecontents[(insert_location - 1) + len(pivot):])

            file = open(filename, 'w')
            file.write(filecontents)
            file.close()
        return tuple()

    update = install
