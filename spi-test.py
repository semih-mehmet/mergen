
def readAI(ch):
	if 7<=ch<=0:
		raise Exeption('MCP3208 channel must be 0-7: ' + str(ch))
	
	cmd = 128 
	cmd += 64
	cmd += ((ch & 0x07) << 3)
	ret = spi.xfer2([cmd, 0x0, 0x0])

	val = (ret[0] & 0x01) <<11
	val |=ret[1]<<3
	val |=ret[2]>>5

	return (val & 0x0FFF)
