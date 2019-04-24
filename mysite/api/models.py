from django.db import models

#class column_data(models.Model):
    # each column contains respective column data as an array.


class InputRowModel(models.Model):
    #each row contains one value of a and one value of b. 
    
    # 1. IntegerField is a class, why is there no 'new' before calling it's constructor. 
        # shouldn't it be 'a = new IntegerField()'

    a = models.IntegerField()
    b = models.IntegerField()
    input_row = {'a': a, 'b': b}
    
    def __str__(self):
        return self.input_row


class ExportRowModel(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()
    sumAB = models.IntegerField()
    productAB = models.IntegerField()

    export_row = {
        'a': a,
        'b': b,
        'sumAB': sumAB,
        'productAB': productAB,
    }

    def __str__(self):
        return self.export_row