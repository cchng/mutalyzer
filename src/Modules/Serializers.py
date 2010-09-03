"""
    Collection of Serilizable Objects used by the webservice
"""
from soaplib.serializers.primitive import String, Integer, Array
from soaplib.serializers.clazz import ClassSerializer
from ZSI import TC
from ZSI.fault import Fault

class SoapMessage(ClassSerializer):
    """
        Send info message over the soapline

        Attributes:
            errorcode   ; The error code affiliated with the error message
            message     ; The error message
    """

    class types():
        errorcode = String
        message = String

    def __init__(self):
        self.typecode = TC.Struct(SoapMessage, [
            TC.String("errorcode"),
            TC.String("message")], "SoapMessage")
#SoapMessage

class Mapping(ClassSerializer) :
    """
        Extended ClassSerializer object with mixed types of attributes

        Attributes:
            startmain ; Define the type of startmain.
            startoffset ; Define the type of startoffset.
            endmain ; Define the type of endmain value.
            endoffset ; Define the type of endoffset value.
            start_g ; Define the type of start_g value.
            end_g ; Define the type of end_g value.
            mutationType ; Define the type of mutation type
    """

    class types() :
        """
            Types are defined here for the soaplib module.
        """

        startmain = Integer
        startoffset = Integer
        endmain = Integer
        endoffset = Integer
        start_g = Integer
        end_g = Integer
        mutationType = String
        errorcode = Integer
        messages = Array(SoapMessage)
    #types

    def __init__(self) :
        """
            Types are defined here for the TC module.
        """

        self.typecode = TC.Struct(Mapping, [
            TC.Integer('startmain'),
            TC.Integer('startoffset'),
            TC.Integer('endmain'),
            TC.Integer('endoffset'),
            TC.Integer('start_g'),
            TC.Integer('end_g'),
            TC.String('mutationType'),
            TC.Integer("errorcode"),
            TC.Array("SoapMessage", TC.Struct(SoapMessage, [
                TC.String("errorcode"),
                TC.String("message")], "SoapMessage"), "messages")
            ], 'Mapping')
    #__init__
#Mapping

class Transcript(ClassSerializer) :
    """
        Extended ClassSerializer object with mixed types of attributes

        Attributes:
            trans_start ; Define the type of trans_start
            trans_stop  ; Define the type of trans_stop
            CDS_stop    ; Define the type of CDS_stop
    """

    class types() :
        """
        """

        trans_start = Integer
        trans_stop = Integer
        CDS_stop = Integer
    #types

    def __init__(self) :
        """
        """

        self.typecode = TC.Struct(Transcript, [
            TC.Integer('trans_start'),
            TC.Integer('trans_stop'),
            TC.Integer('CDS_stop')
            ], 'Transcript')
    #__init__
#Transcript

