function isLetter(str) {
    return /^[A-Za-z]$/.test(str);
}

function populate_input() {
    var element = document.getElementById('wordle-row')
    var val = element.getAttribute('letters')
    var input = document.getElementById('wordle-enter')
    if (!val) {
        val = ''
    }

    input.value = val
}

function populate_entry() {
    var element = document.getElementById('wordle-row')
    var val = element.getAttribute('letters')

    var divs = document.getElementsByName('wordle-col')

    if (val) {
        for (let i = 0; i < 5; i++) {
            if (i < val.length) {
                divs[i].textContent = val[i].toUpperCase()
            } else {
                divs[i].textContent = ''
            }
        }
    } else {
        divs[0].textContent = ''
    }
}

function get_words(parent) {
    var result = []
    for (let child of parent.children) {
        var arr = JSON.parse(child.getAttribute('name').replace(/'/g, '"'));
        if (arr.length == 5) {
            var list = [];
            for (let grand_child of child.children) {
                var classes = grand_child.classList
                var color = classes.contains('yellow') ? 'yellow' : classes.contains('green') ? 'green' : 'none';
                list.push(color);
            }
            result.push([arr, list]);
        }
    }
    return result;
}

function update_db(element) {
    var csrftoken = document.getElementById('csrf-token').getAttribute('content');

    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({action: 'update',
                              words: get_words(element.parentElement.parentElement),
                              })
    })
    .then(response => response.json());
}

function update_color(element) {
    var list = element.classList;

    if (list.contains('yellow')) {
        element.classList.remove('yellow')
        element.classList.add('green')
        update_db(element, 'green')
    } else if (list.contains('green')) {
        element.classList.remove('green')
        update_db(element, 'none')
    } else {
        element.classList.add('yellow')
        update_db(element, 'yellow')
    }
}

document.addEventListener('submit', populate_input);

document.addEventListener('keydown', function(event) {
    var element = document.getElementById('wordle-row')
    var val = element.getAttribute('letters')
    var input = event.key

    if (isLetter(input)) {
        if (val) {
            if (val.length < 5) {
                var new_val = val + input
                element.setAttribute('letters', new_val)
            }
        } else {
            element.setAttribute('letters', input)
        }
    } else if (input == 'Backspace') {
        if (val) {
            var new_val = val.slice(0, -1)
            element.setAttribute('letters', new_val)
        }
    } else if (input == 'Enter') {
        if (val) {
            if (val.length == 5) {
                populate_input()
                var form = document.getElementById('wordle-form')
                form.submit()
            } else {
                alert('Not enough letters')
            }
        } else {
            alert('Not enough letters')
        }
    }

    populate_entry()
});

window.addEventListener('DOMContentLoaded', populate_entry);
