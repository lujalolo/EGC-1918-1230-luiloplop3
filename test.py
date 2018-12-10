data = {
            'type': 'IDENTITY',
            'options': [
                { 'option': 'Option 1', 'number': 1, 'votes': 100 },
                { 'option': 'Option 2', 'number': 2, 'votes': 0 },
                { 'option': 'Option 3', 'number': 3, 'votes': 60 },
                { 'option': 'Option 4', 'number': 4, 'votes': 40 },
                { 'option': 'Option 5', 'number': 5, 'votes': 100 },
                { 'option': 'Option 6', 'number': 6, 'votes': 20 },
            ]
        }

options = data.get('options', [])

out = []
seats = 10

for seat in range(seats):
    opt = max(options, key=lambda opt: opt['votes'])

    if not any(d.get('option', None) == opt['option'] for d in out):
        out.append({
            **opt,
            'postproc': 1,
        });
    else:
        aux = next((o for o in out if o['option'] == opt['option']), None)
        aux['postproc'] = aux['postproc'] + 1

    aux = next((o for o in out if o['option'] == opt['option']), None)
    opt['votes'] = opt['votes']//(aux['postproc'] + 1)

    out.sort(key=lambda x: -x['postproc'])
print(out)
