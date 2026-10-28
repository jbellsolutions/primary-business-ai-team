---
name: honest-chart
description: Build or merge Excel charts without changing the time scale, legend order or data, and prove it with an integrity checklist Chris signs. Use for any chart, graph or "merge these three graphs into one" request.
---

# Honest chart

Serves #50. Chris: ChatGPT "changes the time scale and puts the key backwards", so "the data has no integrity anymore". #52 (gas concentration comparison) is open.

## Inputs
- The Excel workbook as a **copy** Adrielle saves. Never the original, never a screenshot or picture of a chart.
- The sheet, the date column range, and each series' range and unit, named by Chris or Adrielle. Never guess a range.
- `owner.md`: the project's data rule (the lines "Research data in AI tools" and "Participant details in AI tools", ask #90).

## Steps
1. **Data rule first.** A yes in `owner.md` for this project: use Path A. A no: use Path B. Nothing recorded: ask "Is AI allowed on <project>'s data?" in the same message and send only aggregate or de-identified numbers (no names, farm or site identifiers, locations), or use Path B.
2. **Write the spec before drawing:** one row per series with name (exactly the header cell), unit, sheet, x range, y range, colour, panel or axis, and the value-axis minimum and maximum. Adrielle reads it back against the workbook. Only the spec feeds the chart.
3. **Pick the layout with Chris** ("split the scale"). Stacked panels on one shared time axis is the default when units differ. One chart with a left and a right value axis works for two units only: colour each axis title to match its series and say which series sits where. Use one axis when units match. No broken axes. Log scale only if Chris asks, titled "log scale".
4. **Time.** The date column must hold real dates, not text. Plot on a true date axis so uneven sampling looks uneven. No resampling, smoothing, averaging or filled gaps. A blank cell is a gap, never a zero.
5. **Axes.** Set each value axis minimum and maximum by hand, and write them on the checklist. Bars start at zero. Lines may start higher if the axis says so. Units in every axis title. Never invert an axis.
6. **Key.** Legend order equals the spec order and the visual order. Colours stay the same for a series in every panel.
7. **Comparisons are calculations.** If Chris wants readings compared, compute the figures in Excel or code, show the cells, and never read them off a picture.
8. **Path A (data cleared):** read the cells with code from the copy, draw from them, then run this check on the finished figure. Paste its output unedited. If anything FAILs, fix the cause and rerun from the start. Never retype or "adjust" a number.
```python
import math, datetime as dt, openpyxl
def read(path, spec):                      # spec rows: name, unit, sheet, x, y (cell ranges), color
    wb = openpyxl.load_workbook(path, data_only=True)       # the COPY, never the original
    cells = lambda sh, r: [c.value for row in wb[sh][r] for c in row]
    return [dict(s, x=cells(s["sheet"], s["x"]),
                 y=[math.nan if v is None else v for v in cells(s["sheet"], s["y"])]) for s in spec]  # blank = gap, never 0
def check(fig, spec, path):                # re-reads the workbook, compares it with the chart object (matplotlib 3.7+)
    res, src = [], read(path, spec)
    def t(ok, what): res.append(("PASS" if ok else "FAIL", what))
    lines = [l for ax in fig.axes for l in ax.get_lines()]
    t(len(lines) == len(src), f"{len(lines)} lines drawn, {len(src)} series in the spec")
    for s, l in zip(src, lines):
        n = sum(not math.isnan(v) for v in s["y"]); y = list(l.get_ydata(orig=True)); lo, hi = l.axes.get_ylim()
        t(all(isinstance(v, (dt.datetime, dt.date, int, float)) for v in s["x"]), f'{s["name"]}: x values are real dates or numbers, not text')
        t(list(l.get_xdata(orig=True)) == s["x"], f'{s["name"]}: every x value equals its source cell')
        t(len(y) == len(s["y"]) and all(a == b or (math.isnan(a) and math.isnan(b)) for a, b in zip(y, s["y"])),
          f'{s["name"]}: every y equals its source cell; n={n} of {len(y)}, blanks left as gaps')
        t(lo <= min(v for v in s["y"] if v == v) and max(v for v in s["y"] if v == v) <= hi, f'{s["name"]}: axis {lo:g} to {hi:g} holds all points')
        t(s["unit"] in l.axes.get_ylabel(), f'{s["name"]}: axis label carries the unit "{s["unit"]}"')
    lg = (fig.legends or [a.get_legend() for a in fig.axes if a.get_legend()])[0]
    t([x.get_text() for x in lg.get_texts()] == [s["name"] for s in spec], "legend order equals the spec order")
    t([h.get_color() for h in lg.legend_handles] == [s["color"] for s in spec], "legend colours match the series")
    return res
```
9. **Path B (a person builds it in Excel):** give click-by-click steps for the spec: series in adjacent columns under one date column; a scatter chart with straight lines, or a line chart with the axis type set to Date axis; Select Data to order the series; the secondary axis set on the series; empty cells shown as gaps. Menu names vary by version, so ask Adrielle what she sees. She then reads off axis type, minimum and maximum, legend order, each series' range from Select Data, and the point count. Compare each with the spec, line by line.
10. **Checks sheet.** Either path: give Adrielle formulas for a Checks sheet in the copy (COUNT, MIN, MAX and the first and last cell for each range). Excel computes the numbers, not the model.

## Output
The spec, the chart file, the checklist (one row per series and per axis: source range, unit, n, blanks, first, last, min, max, axis range, axis type, legend position; each PASS, FAIL or UNKNOWN with evidence), and the sign-off line: "Chart <name>. Checked against <file, date>. Signed off by Chris on <date>: '<his words>'". Adrielle saves them together (SOP 28).

## Done when
Every row is PASS or a UNKNOWN Chris has accepted, and Chris has said yes to this exact chart. A chart that failed the checklist is not shown outside the business.

## Never
- Redraw from a picture, from memory or from numbers typed into the chat.
- Change, round, smooth, resample or fill any source value, or alter the original workbook.
- Reorder the key, or change the time scale to make the chart look better.
- Present an unsigned chart.
