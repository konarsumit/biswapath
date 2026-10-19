# BiswaPath subject-wise university finder: data structure (draft, 19 Oct 2026)

This folder prepares a searchable finder for students who know what they want to study but not where to apply.
Phase 1 covers the UK, Germany and the USA. Bangladesh (as a source country) and other destinations follow.

## Files

| File | What it holds |
|---|---|
| `subjects.json` | The 11 BiswaPath subject categories, mapped to each country's official classification (HESA CAH, Destatis Fächergruppe, US CIP). |
| `schema.json` | JSON Schema for one record: one university × one subject × one degree level. |
| `records.sample.json` | Example records showing how fields are filled, including the "no data" cases. |
| `../stats/indicators.json` | Every statistic shown on the Statistics page, with measure type, period and source. |

## Rules (these apply to every record)

1. **Two kinds of evidence are never mixed.**
   - `indian_enrolment` is filled only from a published source that counts Indian students for that university **and** subject (for example a university's own statistics page, or a HESA custom dataset). Otherwise `value` stays `null` and `status` explains why.
   - `subject_rank` holds ranking information (e.g. QS by Subject). It describes subject strength, never popularity with Indian students.
2. **Measure types are explicit**: `enrolment`, `opt_participants`, `visa_grants`, `government_estimate`, `ranking`. Totals of different types are never added together.
3. **Every number has** a reference period, a source URL, a `source_kind` (`primary` = the body that produced it; `secondary` = a report of it) and a `checked` date.
4. **No invented numbers, no popularity rankings** unless built from verified `indian_enrolment` values for the same period and measure.
5. Bengali text fields (`name_bn`, `note_bn`) are optional; English names of universities and programmes stay in English.

## What the open data can and cannot give (status values)

| `status` | Meaning |
|---|---|
| `verified` | Published figure found at the source and checked. |
| `not_published` | No open source publishes this combination (e.g. HESA does not cross university × subject × country in open data). |
| `custom_request_needed` | Available only through a paid/custom data request (e.g. Jisc/HESA tailored data). |
| `university_publishes` | The university publishes its own nationality statistics; figure still to be extracted. |
| `pending_check` | A figure exists in a secondary source but has not been confirmed at the original source. |

## Next steps

1. Fill `programmes` for the 49 universities already in `../universities.json`, starting with UK/Germany/USA.
2. Collect `subject_rank` from official QS/THE subject tables, citing the edition.
3. Search each university's own statistics pages for nationality × subject tables (`university_publishes`).
4. Collect Bengali-student answers through the Contribute form; publish counts only (never names), with `measure_type: "biswapath_survey"`.
