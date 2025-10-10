#ifndef COLABORADOR_H
#define COLABORADOR_H

#include "utils.h"

char* VerTodosLosColaboradores(const char *url);
enum MHD_Result URLColaborador
(const char *url, const char *method, struct MHD_Connection *conn);

#endif
