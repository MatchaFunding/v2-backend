#ifndef MIEMBRO_H
#define MIEMBRO_H

#include "utils.h"

char* VerTodosLosMiembros(const char *url);
enum MHD_Result URLMiembro
(const char *url, const char *method, struct MHD_Connection *conn);

#endif
