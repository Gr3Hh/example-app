{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "app.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "app.labels" -}}
helm.sh/chart: {{ include "app.chart" . }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{ include "app.selectorLabels" . }}
{{- end }}

{{- define "app.selectorLabels" -}}
release: {{ .Release.Name }}
app: hello-world
{{- end }}


{{- define "app.env" }}
env:
  - name: POSTGRES_HOST
    value: "{{ .Values.postgres.host }}"
  - name: POSTGRES_DB
    value: {{ .Values.postgres.db }}
  - name: POSTGRES_USER
    value: {{ .Values.postgres.user }}
  - name: POSTGRES_PASSWORD
    valueFrom:
      secretKeyRef:
        name: "postgresql"
        key: postgresql-password
{{- end }}
