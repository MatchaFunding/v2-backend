#ifndef RESULTADO_H
#define RESULTADO_H

#include "utils.h"

char* VerResultados(const char *url);
enum MHD_Result URLResultado
(const char *url, const char *method, struct MHD_Connection *conn);

#endif
