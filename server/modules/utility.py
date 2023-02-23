import json

# Simple Json cleanup utility
def sanitizeJson(input):
    output = str(input).replace("'", "\"")
    return json.loads(output)

# Convert value from range 1 to corresponding value in range 2
# Usage: x = convertRange( 10, [0, 20], [0, 200]), x = 100.0
def convertRange( value, r1, r2 ):
    return ( value - r1[ 0 ] ) * ( r2[ 1 ] - r2[ 0 ] ) / ( r1[ 1 ] - r1[ 0 ] ) + r2[ 0 ];