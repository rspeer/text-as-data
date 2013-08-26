
In[1]:

```
import requests
import json
```

In[2]:

```
BASE = 'http://conceptnet5.media.mit.edu/data/5.1'
```

In[3]:

```
def conceptnet_lookup(uri):
    return requests.get(BASE + uri).json()
```

In[20]:

```
for edge in conceptnet_lookup('/c/en/learn')['edges']:
    print [edge['rel'], edge['start'], edge['end']]
```


    [u'/r/DerivedFrom', u'/c/en/learn/v/gain_knowledge_or_skills', u'/c/en/learn/n/the_cognitive_process_of_acquiring_skill_or_knowledge']
    [u'/r/DerivedFrom', u'/c/en/learn', u'/c/en/learn/v']
    [u'/r/Causes', u'/c/en/teach/v/impart_skills_or_knowledge_to', u'/c/en/learn/v/gain_knowledge_or_skills']
    [u'/r/Entails', u'/c/en/master/v/be_or_become_completely_proficient_or_skilled_in', u'/c/en/learn/v/gain_knowledge_or_skills']
    [u'/r/IsA', u'/c/en/relearn/v/learn_something_again,_as_after_having_forgotten_or_neglected_it', u'/c/en/learn/v/gain_knowledge_or_skills']
    [u'/r/IsA', u'/c/en/study/n/applying_the_mind_to_learning_and_understanding_a_subject_', u'/c/en/learn/n/the_cognitive_process_of_acquiring_skill_or_knowledge']
    [u'/r/IsA', u'/c/en/study/v/learn_by_reading_books', u'/c/en/learn/v/gain_knowledge_or_skills']
    [u'/r/SimilarTo', u'/c/en/learn/v/get_to_know_or_become_aware_of,_usually_accidentally', u'/c/en/witness/v/perceive_or_be_contemporaneous_with']
    [u'/r/IsA', u'/c/en/train/v/undergo_training_or_instruction_in_preparation_for_a_particular_role,_function,_or_profession', u'/c/en/learn/v/be_a_student_of_a_certain_subject']
    [u'/r/IsA', u'/c/en/transfer/n/application_of_a_skill_learned_in_one_situation_to_a_different_but_similar_situation', u'/c/en/learn/n/the_cognitive_process_of_acquiring_skill_or_knowledge']
    [u'/r/IsA', u'/c/en/trip_up/v/detect_a_blunder_or_misstep', u'/c/en/learn/v/get_to_know_or_become_aware_of,_usually_accidentally']
    [u'/r/IsA', u'/c/en/wise_up/v/get_wise_to', u'/c/en/learn/v/get_to_know_or_become_aware_of,_usually_accidentally']
    [u'/r/DerivedFrom', u'/c/en/learn/v/be_a_student_of_a_certain_subject', u'/c/en/study/n/applying_the_mind_to_learning_and_understanding_a_subject_']
    [u'/r/DerivedFrom', u'/c/en/learn/v/be_a_student_of_a_certain_subject', u'/c/en/discipline/n/a_branch_of_knowledge']
    [u'/r/DerivedFrom', u'/c/en/learn/v/be_a_student_of_a_certain_subject', u'/c/en/perusal/n/reading_carefully_with_intent_to_remember']
    [u'/r/DerivedFrom', u'/c/en/learn/v/get_to_know_or_become_aware_of,_usually_accidentally', u'/c/en/discovery/n/the_act_of_discovering_something']
    [u'/r/DerivedFrom', u'/c/en/learn/v/get_to_know_or_become_aware_of,_usually_accidentally', u'/c/en/discovery/n/something_that_is_discovered']
    [u'/r/DerivedFrom', u'/c/en/learn/v/get_to_know_or_become_aware_of,_usually_accidentally', u'/c/en/discovery/n/a_productive_insight']
    [u'/r/DerivedFrom', u'/c/en/learn/v/gain_knowledge_or_skills', u'/c/en/learner/n/someone_who_learns_or_takes_up_knowledge_or_beliefs']
    [u'/r/DerivedFrom', u'/c/en/learn/v/gain_knowledge_or_skills', u'/c/en/apprentice/n/works_for_an_expert_to_learn_a_trade']
    [u'/r/DerivedFrom', u'/c/en/get/v/come_into_the_possession_of_something_concrete_or_abstract', u'/c/en/learn/n/the_cognitive_process_of_acquiring_skill_or_knowledge']
    [u'/r/DerivedFrom', u'/c/en/learn/v/gain_knowledge_or_skills', u'/c/en/skill/n/an_ability_that_has_been_acquired_by_training']
    [u'/r/RelatedTo', u'/c/en/discover/v/make_a_discovery', u'/c/en/learn/v/get_to_know_or_become_aware_of,_usually_accidentally']
    [u'/r/RelatedTo', u'/c/en/pick/v/look_for_and_gather', u'/c/en/learn/v/get_to_know_or_become_aware_of,_usually_accidentally']
    [u'/r/IsA', u'/c/en/absorb/v/take_up_mentally', u'/c/en/learn/v/gain_knowledge_or_skills']
    [u'/r/IsA', u'/c/en/ascertain/v/learn_or_discover_with_certainty', u'/c/en/learn/v/get_to_know_or_become_aware_of,_usually_accidentally']
    [u'/r/IsA', u'/c/en/audit/v/attend_academic_courses_without_getting_credit', u'/c/en/learn/v/be_a_student_of_a_certain_subject']
    [u'/r/IsA', u'/c/en/catch_up/v/learn_belatedly', u'/c/en/learn/v/gain_knowledge_or_skills']
    [u'/r/IsA', u"/c/en/condition/n/a_learning_process_in_which_an_organism's_behavior_becomes_dependent_on_the_occurrence_of_a_stimulus_in_its_environment", u'/c/en/learn/n/the_cognitive_process_of_acquiring_skill_or_knowledge']
    [u'/r/IsA', u'/c/en/developmental_learn/n/learning_that_takes_place_as_a_normal_part_of_cognitive_development', u'/c/en/learn/n/the_cognitive_process_of_acquiring_skill_or_knowledge']
    [u'/r/IsA', u'/c/en/digestion/n/learning_and_coming_to_understand_ideas_and_information', u'/c/en/learn/n/the_cognitive_process_of_acquiring_skill_or_knowledge']
    [u'/r/IsA', u'/c/en/discover/v/make_a_discovery', u'/c/en/learn/v/get_to_know_or_become_aware_of,_usually_accidentally']
    [u'/r/IsA', u'/c/en/drill/v/learn_by_repetition', u'/c/en/learn/v/be_a_student_of_a_certain_subject']
    [u'/r/IsA', u'/c/en/education/n/the_gradual_process_of_acquiring_knowledge', u'/c/en/learn/n/the_cognitive_process_of_acquiring_skill_or_knowledge']
    [u'/r/IsA', u'/c/en/get_good/v/discover_some_bad_or_hidden_information_about', u'/c/en/learn/v/get_to_know_or_become_aware_of,_usually_accidentally']
    [u'/r/IsA', u'/c/en/imprint/n/a_learning_process_in_early_life_whereby_species_specific_patterns_of_behavior_are_established', u'/c/en/learn/n/the_cognitive_process_of_acquiring_skill_or_knowledge']
    [u'/r/IsA', u'/c/en/internalization/n/learning_that_is_incorporated_within_yourself', u'/c/en/learn/n/the_cognitive_process_of_acquiring_skill_or_knowledge']
    [u'/r/IsA', u'/c/en/language_learn/n/learning_to_use_a_language', u'/c/en/learn/n/the_cognitive_process_of_acquiring_skill_or_knowledge']
    [u'/r/IsA', u'/c/en/learn/n/the_cognitive_process_of_acquiring_skill_or_knowledge', u'/c/en/basic_cognitive_process/n/cognitive_processes_involved_in_obtaining_and_storing_knowledge']
    [u'/r/IsA', u'/c/en/memorization/n/learning_so_as_to_be_able_to_remember_verbatim', u'/c/en/learn/n/the_cognitive_process_of_acquiring_skill_or_knowledge']
    [u'/r/Synonym', u'/c/en/study', u'/c/en/learn/v']
    [u'/r/DerivedFrom', u'/c/en/learner', u'/c/en/learn/v']
    [u'/r/ConceptuallyRelatedTo', u'/c/en/larn', u'/c/en/learn/v']
    [u'/r/ConceptuallyRelatedTo', u'/c/en/lore', u'/c/en/learn/v']
    [u'/r/Synonym', u'/c/en/learn', u'/c/en/read/v']
    [u'/r/Synonym', u'/c/en/brainy', u'/c/en/learn/a']
    [u'/r/DerivedFrom', u'/c/en/learnedly', u'/c/en/learn/a']
    [u'/r/DerivedFrom', u'/c/en/learnedness', u'/c/en/learn/a']
    [u'/r/Synonym', u'/c/en/learn', u'/c/en/knowledge/n']
    [u'/r/DerivedFrom', u'/c/en/book-learning', u'/c/en/learn/n']


In[21]:

```
conceptnet_lookup('/assoc/list/en/good@1,bad@-1')
```




    {u'similar': [[u'/c/sv/trevlig', 0.2688268154152955],
      [u'/c/gd/c\xe0ilear', 0.2660558866527395],
      [u'/c/ru/\u043f\u0440\u0438\u044f\u0442\u043d\u043e', 0.2660214209709472],
      [u'/c/nl/leuk', 0.26547708333799425],
      [u'/c/en/well-known', 0.2650954284862889],
      [u'/c/pl/mi\u0142y', 0.263279346770283],
      [u'/c/en/pleasant/a/giving_pleasure', 0.263253873083068],
      [u'/c/hi/\u0938\u0941\u0902\u0926\u0930', 0.2631417469366888],
      [u'/c/fr/bienvenu', 0.26292641855993676],
      [u'/c/la/festivus', 0.2624196420624598],
      [u'/c/sw/zuri', 0.26220550614025895],
      [u'/c/en/delectable', 0.2618771681543707],
      [u'/c/da/dejlig', 0.2618431055168956],
      [u'/c/it/simpatico', 0.26125208554341967],
      [u'/c/fr/agr\xe9able', 0.2610676171428799],
      [u'/c/da/heldig', 0.26073129816572427],
      [u'/c/nl/aangenam', 0.26037714049752225],
      [u"/c/en/welcome/i/greeting_given_upon_someone's_arrival",
       0.26028615841057795],
      [u'/c/hy/\u057d\u056b\u0580\u0578\u0582\u0576', 0.25968853199690617],
      [u'/c/hu/szimpatikus', 0.25967794633315716]],
     u'terms': [[u'/c/en/good', 1.0], [u'/c/en/bad', -1.0]]}



In[22]:

```
conceptnet_lookup('/assoc/list/en/good@-1,bad@1?filter=/c/en')
```




    {u'similar': [[u'/c/en/bad_case', 0.34464397929311263],
      [u'/c/en/extreme_anger', 0.3358060742731915],
      [u'/c/en/hitman', 0.32772202879752116],
      [u'/c/en/incorrect_belief', 0.32453348558507095],
      [u'/c/en/psychopath', 0.3239106054566913],
      [u'/c/en/stab_to_death', 0.3223237849451443],
      [u'/c/en/harden_criminal', 0.3218490788087544],
      [u'/c/en/pernicious', 0.32077089429888117],
      [u'/c/en/dangerous/a/full_of_danger', 0.3181899553923286],
      [u'/c/en/unsafe', 0.318023315315224],
      [u'/c/en/threat', 0.3160851740719441],
      [u'/c/en/perilous/a/Dangerous,_full_of_peril', 0.3160699757547605],
      [u'/c/en/i_thwart', 0.3154224070987765],
      [u'/c/en/hide_evidence', 0.31235451852430135],
      [u'/c/en/dangerously', 0.31233575306985806],
      [u'/c/en/dangerous/a', 0.3115220446669545],
      [u'/c/en/break_law', 0.31129209068059727],
      [u'/c/en/see_psychiatrist', 0.31107864309016453],
      [u'/c/en/whip/v/to_urge_into_action', 0.3094217693659347],
      [u'/c/en/bad_thing', 0.30938331778831707]],
     u'terms': [[u'/c/en/good', -1.0], [u'/c/en/bad', 1.0]]}



In[23]:

```
conceptnet_lookup('/assoc/c/en/ship?filter=/c/en')
```




    {u'similar': [[u'/c/en/ship', 0.9992869025794743],
      [u'/c/en/boater', 0.9848146724131737],
      [u'/c/en/on_boat', 0.9843651252702114],
      [u'/c/en/ship_boat', 0.9799873106083218],
      [u'/c/en/boat_ship', 0.9772575506605697],
      [u'/c/en/ship/n/large_water_vessel', 0.9770333490933658],
      [u'/c/en/nave/n/the_middle_or_body_of_a_church', 0.9691869541235387],
      [u'/c/en/sail_ship', 0.9672654011920178],
      [u'/c/en/steer_ship', 0.9658451591399131],
      [u'/c/en/vessel/n/craft', 0.9652412090910628],
      [u'/c/en/one_instance_of_vessel', 0.9648123088384739],
      [u'/c/en/mainsail', 0.9643985375417666],
      [u'/c/en/large_boat', 0.9643759140669548],
      [u'/c/en/seaman', 0.9640026637353616],
      [u'/c/en/boat/n/water_craft', 0.9631682151572668],
      [u'/c/en/navigator', 0.960013491892171],
      [u'/c/en/on_ship', 0.9588013714554242],
      [u'/c/en/keel', 0.9550469539167159],
      [u'/c/en/big_boat', 0.9538301789780692],
      [u'/c/en/stalin', 0.9534793439678204]],
     u'terms': [[u'/c/en/ship', 1.0]]}



In[ ]:

```

```
