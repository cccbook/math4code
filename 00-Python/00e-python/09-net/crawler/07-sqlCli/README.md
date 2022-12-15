# sqlCli

```
$ python sqlCli.py
sql:SELECT * FROM stockPrice
('111/10/03', 418.5, 417, 70127)
('111/10/04', 429.5, 429, 31696)
('111/10/05', 444.5, 445, 51865)
('111/10/06', 450.5, 451, 24907)
('111/10/07', 448.5, 438, 45112)
('111/10/11', 408, 401.5, 210614)
('111/10/12', 397, 397.5, 114055)
('111/10/13', 400.5, 395, 66846)
('111/10/14', 414.5, 412, 54666)
('111/10/17', 400, 397, 66589)
('111/10/18', 406.5, 407, 30538)
('111/10/19', 404, 395.5, 68211)
('111/10/20', 391, 397.5, 76430)
('111/10/21', 395.5, 389.5, 64043)
sql:SELECT * FROM stockPrice ORDER BY 收盤價 DESC
('111/10/06', 450.5, 451, 24907)
('111/10/05', 444.5, 445, 51865)
('111/10/07', 448.5, 438, 45112)
('111/10/04', 429.5, 429, 31696)
('111/10/03', 418.5, 417, 70127)
('111/10/14', 414.5, 412, 54666)
('111/10/18', 406.5, 407, 30538)
('111/10/11', 408, 401.5, 210614)
('111/10/12', 397, 397.5, 114055)
('111/10/20', 391, 397.5, 76430)
('111/10/17', 400, 397, 66589)
('111/10/19', 404, 395.5, 68211)
('111/10/13', 400.5, 395, 66846)
('111/10/21', 395.5, 389.5, 64043)
sql:SELECT * FROM stockPrice WHERE 收盤價>410     
('111/10/03', 418.5, 417, 70127)
('111/10/04', 429.5, 429, 31696)
('111/10/05', 444.5, 445, 51865)
('111/10/06', 450.5, 451, 24907)
('111/10/07', 448.5, 438, 45112)
('111/10/14', 414.5, 412, 54666)
sql:exit
```