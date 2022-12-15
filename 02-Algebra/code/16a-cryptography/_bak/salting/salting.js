import * as bcrypt from "https://deno.land/x/bcrypt@v0.2.4/mod.ts" 
 salt = bcrypt.genSaltSync(10) 
 hash = bcrypt.hashSync("mypassword", salt) 
print('hash=', hash)
