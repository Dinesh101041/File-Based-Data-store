## File  basedkey value data store  

    1. It can be initialized using an optional file path. If one is not provided, it will reliably create itself in a reasonable location on the laptop.<br>

    2.A new key-value pair can be added to the data store using the Create operation. The key is always a string - capped at 32chars. The value is always a JSON object - capped at 16KB.<br>

    3.If Create is invoked for an existing key, an appropriate error will be returned.<br>

    4.A Read operation on a key can be performed by providing the key, and receiving the value in response, as a JSON object.<br>

    5.A Delete operation can be performed by providing the key.<br>

    6.Every key supports setting a Time-To-Live property when it is created. This property is optional. If provided, it will be evaluated as an integer defining the number of seconds the key must be retained in the data store. Once the Time-To-Live for a key has expired, the key will no longer be available for Read or Delete operations.<br>

    7. Appropriate error responses must always be returned to a client if it uses the data store in unexpected ways or breaches any limits<br>

    8.The file size never exceeds 1GB

        

    
