from django.db import models


class ErrorType(models.Model):
    errorType = models.CharField(max_length=255)
    package = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=50)
    severity = models.CharField(max_length=20)
    generalExplanation = models.TextField(max_length=3000)
    generalFix = models.TextField(max_length=3000)
    docsUrl = models.URLField(max_length=500, blank=True)
    upVotes = models.PositiveIntegerField(default=0)
    downVotes = models.PositiveIntegerField(default=0)
    wilsonScore = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )
    createdByAI = models.BooleanField(default=True)
    AiModel = models.CharField(max_length=100, null=True, blank=True)
    fingerPrint = models.CharField(max_length=64, db_index=True)


class ErrorCase(models.Model):
    caseName = models.CharField(max_length=255)
    explanation = models.TextField(max_length=3000)
    fix = models.TextField(max_length=3000)
    example = models.TextField(max_length=3000)
    severity = models.CharField(max_length=20)
    AiModel = models.CharField(max_length=100, null=True, blank=True)
    fingerPrint = models.CharField(
        max_length=64,
        unique=True,
        db_index=True
    )
    ErrorTypeID = models.ForeignKey(
        ErrorType,
        on_delete=models.PROTECT,
        related_name="cases"
    )
    # error_type_id INTEGER NOT NULL,

    # case_name TEXT,

    # pattern TEXT NOT NULL,

    # explanation_beginner TEXT NOT NULL,
    # explanation_intermediate TEXT,
    # explanation_advanced TEXT,

    # fix TEXT,
    # example TEXT,

    # severity_override TEXT,

    # created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    # FOREIGN KEY (error_type_id) REFERENCES error_types(id));
# Create your models here.
