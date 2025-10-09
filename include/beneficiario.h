#ifndef BENEFICIARIO_H
#define BENEFICIARIO_H

#include "utils.h"

char* VerTodosLosBeneficiarios(const char *url);
enum MHD_Result URLBeneficiario
(const char *url, const char *method, struct MHD_Connection *conn);

#endif
