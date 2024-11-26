symptom(amit, fever).
symptom(amit, rash).

has_symptoms(X, cold) :- symptom(X, fever), symptom(X, rash).

diagnose(X, Disease) :- has_symptoms(X, Disease), disease(Disease).
