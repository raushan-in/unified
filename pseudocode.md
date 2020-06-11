INIT Array

FOR source1_each_hotel in source1
    FOR source2_each_hotel in source2
        IF name, location exactly match
            Array := source2_each_hotel
            break
        ELSE IF name AND location partially match
            Array := source2_each_hotel
            break
        ELSE
            Array := source1_each_hotel
        ENDIF
    ENDFOR
ENDFOR

IF source2 EXIST:
    FOR source2_each_hotel in source2
        Array := source2_each_hotel
    ENDFOR
ENDIF

RETURN Array



