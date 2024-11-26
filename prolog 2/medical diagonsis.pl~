symptom(john, fever).
symptom(john, cough).
symptom(mary, headache).
symptom(mary, fever).
symptom(alice, sore_throat).
symptom(alice, cough).

disease(flue).
disease(cold).
disease(strep_throat).

has_symptoms(X, flue) :- symptom(X, fever), symptom(X, cough).
has_symptoms(X, cold) :- symptom(X, headache), symptom(X, sore_throat), not(has_symptoms(X, flue)).
has_symptoms(X, strep_throat) :- symptom(X, sore_throat), symptom(X, fever), not(has_symptoms(X, flue)).

diagnose(X, Disease) :- has_symptoms(X, Disease), disease(Disease).
