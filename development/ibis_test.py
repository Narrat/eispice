import eispice
ibs = eispice.Ibis('test')
cct = eispice.Circuit('IBIS Test')
cct.Driver = ibs['2']('vs')
cct.Rt = eispice.R('vs', 'vi', 33.2)
cct.Tg = eispice.T('vi', 0, 'vo', 0, 50, '2n')
cct.Receiver = ibs['1']('vo')
cct.tran('0.01n', '20n')
eispice.plot(cct)
