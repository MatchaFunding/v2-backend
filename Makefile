all:
	gcc src/*.c src/view/*.c src/controller/*.c -Wall -lmicrohttpd -lmariadb -lcurl -lcjson -lhiredis -O3 -o bin/out
