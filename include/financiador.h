#ifndef FINANCIADOR_H
#define FINANCIADOR_H

#include "utils.h"

char* VerTodosLosFinanciadores(const char *url);
enum MHD_Result URLFinanciador
(const char *url, const char *method, struct MHD_Connection *conn);

#endif
