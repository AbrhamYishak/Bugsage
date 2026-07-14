from django.db import models
class ErrorType(models.Model):
    errorType = models.CharField()
    package = models.CharField()
    category = models.CharField()
    severity = models.CharField()
    generalExplanation = models.CharField()
    generalFix = models.CharField()
    docsUrl = models.CharField()
    upVotes = models.IntegerField(default=0)
    downVotes = models.IntegerField(default=0)
    wilsonScore = models.DecimalField(decimal_places= 2,max_digits=5,default=0)
    createdByAI = models.BooleanField(default=True)
    
class ErrorCase(models.Model):
    caseName = models.CharField()
    explanation = models.CharField()
    fix = models.CharField()
    example = models.CharField()
    severity = models.CharField()
    ErrorTypeID = models.ForeignKey(ErrorType,on_delete = models.PROTECT,related_name = "cases")
  
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
