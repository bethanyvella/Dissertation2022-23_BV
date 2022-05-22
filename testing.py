import hashlib

fileurlOfficial = "C:\\Users\\betha\\Desktop\\JQueries\\2.0.0\\minifed\\jquery-2.1.1.min.js"
fileurlTest = "websites\\msn.com\\__static-global-s-msn-com.akamaized.net_hp-neu__h_975a7d20_webcore_externalscripts_jquery_jquery-2.1.1.min.js"


with open(test, 'rb') as jsScript:
                    file_buffer = jsScript.read()
                    result = hashlib.sha256(file_buffer)
                    print("Official")
                    print(result.hexdigest())
                        

with open(fileurlTest, 'rb') as jsScript:
                    file_buffer = jsScript.read()
                    result = hashlib.sha256(file_buffer)
                    print("Test from MSN")
                    print(result.hexdigest())
                        
                        