#ifndef INSTRUMENTO_H
#define INSTRUMENTO_H

#include "utils.h"

char* VerTodosLosInstrumentos(const char *url);
enum MHD_Result URLInstrumento
(const char *url, const char *method, struct MHD_Connection *conn);

#endif
