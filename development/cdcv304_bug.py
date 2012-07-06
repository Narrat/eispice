import eispice
ibs = eispice.Ibis('cdcv304.ibs' , 'cDcv304(3.3v_clock_driver)')
#~ cct = eispice.Circuit('IBIS Test')
#~ cct.Vx = eispice.V('vs',0, 10, eispice.Pulse(0, 2.5,
#~ '0n','0.1n','0.1n','4n','8n'))
#~ cct.Rt = eispice.R('vs', 'vi', 50)
#~ cct.Tg = eispice.T('vi', 0, 'vo', 0, 50, '1n')
#~ cct.Receiver = ibs['1']('vo', modelName = 'CDCV304_OUT')
#~ cct.tran('0.01n', '18n')
#~ eispice.plot(cct)

help(ibs['1'])
