import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct
    
def test_add_multiple_choices():
    q = Question("Pergunta?", 1)
    q.add_choice("Opção A", False)
    q.add_choice("Opção B", True)
    assert len(q.choices) == 2

def test_remove_choice_by_id():
    q = Question("Pergunta?", 1)
    choice = q.add_choice("Opção A")
    q.remove_choice_by_id(choice.id)
    assert len(q.choices) == 0
    
def test_remove_all_choices():
    q = Question("Pergunta?", 1)
    q.add_choice("Opção A")
    q.add_choice("Opção B")
    q.remove_all_choices()
    assert q.choices == []

def test_select_only_correct_choices():
    q = Question("Pergunta?", 1, max_selections=2)
    c1 = q.add_choice("Errada", False)
    c2 = q.add_choice("Certa", True)
    selected = q.select_choices([c1.id, c2.id])
    assert selected == [c2.id]

def test_select_more_than_max_selections():
    q = Question("Pergunta?", 1, max_selections=1)
    c1 = q.add_choice("Opção A")
    c2 = q.add_choice("Opção B")
    with pytest.raises(Exception, match="Cannot select more than 1 choices"):
        q.select_choices([c1.id, c2.id])

def test_set_correct_choices():
    q = Question("Pergunta?", 1)
    c1 = q.add_choice("Opção A", False)
    q.set_correct_choices([c1.id])
    assert c1.is_correct

def test_create_choice_with_empty_text():
    q = Question("Pergunta?", 1)
    with pytest.raises(Exception, match="Text cannot be empty"):
        q.add_choice("")

def test_create_choice_with_long_text():
    q = Question("Pergunta?", 1)
    long_text = "a" * 101
    with pytest.raises(Exception, match="Text cannot be longer than 100 characters"):
        q.add_choice(long_text)

def test_question_invalid_points():
    with pytest.raises(Exception, match="Points must be between 1 and 100"):
        Question("Pergunta?", 0)
    with pytest.raises(Exception, match="Points must be between 1 and 100"):
        Question("Pergunta?", 101)

def test_choices_have_sequential_ids():
    q = Question("Pergunta?", 1)
    c1 = q.add_choice("Opção A")
    c2 = q.add_choice("Opção B")
    c3 = q.add_choice("Opção C")
    assert c1.id == 1
    assert c2.id == 2
    assert c3.id == 3

