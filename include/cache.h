#ifndef CACHE_H
#define CACHE_H

#define CACHE_HOST "127.0.0.1"
#define CACHE_PORT 6379

char *BuscarEnCache(const char *key);
void GuardarEnCache(const char *key, const char *value);

#endif
