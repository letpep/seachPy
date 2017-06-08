#
# $Id$
#
#!/usr/bin/python3
#coding=utf-8
from sphinxapi import *
import sys, time


class searchQ(object):
    def search(self,qm="111"):
        q = ''
        mode = SPH_MATCH_ALL
        host = '59.110.213.45'
        port = 9312
        index = '*'
        filtercol = 'group_id'
        filtervals = []
        sortby = ''
        groupby = ''
        groupsort = '@group desc'
        limit = 0
        q = '%s%s ' % (q, qm)

        # do query
        cl = SphinxClient()
        cl.SetServer(host, port)
        cl.SetWeights([100, 1])
        cl.SetMatchMode(mode)
        if filtervals:
            cl.SetFilter(filtercol, filtervals)
        if groupby:
            cl.SetGroupBy(groupby, SPH_GROUPBY_ATTR, groupsort)
        if sortby:
            cl.SetSortMode(SPH_SORT_EXTENDED, sortby)
        if limit:
            cl.SetLimits(0, limit, max(limit, 1000))
        res = cl.Query(q, index)
        return res

        if not res:
            return  2

        if cl.GetLastWarning():
            print
            'WARNING: %s\n' % cl.GetLastWarning()

        print
        'Query \'%s\' retrieved %d of %d matches in %s sec' % (q, res['total'], res['total_found'], res['time'])
        print
        'Query stats:'

        if res.has_key('words'):
            for info in res['words']:
                print
                '\t\'%s\' found %d times in %d documents' % (info['word'], info['hits'], info['docs'])

            print
            '\nMatches:'

            return
            '%d. doc_id=%s, weight=%d%s' % (1, 2, 3, res['matches'])
