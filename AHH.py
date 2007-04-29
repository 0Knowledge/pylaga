def ahh(die):
    import traceback,sys
    type, info, trace = sys.exc_info()
    tracetop = traceback.extract_tb(trace)[-1]
    tracetext = 'File %s, Line %d' % tracetop[:2]
    if tracetop[2] != '?':
        tracetext += ', Function %s' % tracetop[2]
    exception_message = '%s:\n%s\n\n%s\n"%s"'
    message = exception_message % (str(type), str(info), tracetext, tracetop[3])
    if type not in (KeyboardInterrupt, SystemExit):
        print message
    raise
    if die:
	    sys.exit(1)
	    