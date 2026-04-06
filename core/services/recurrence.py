# from datetime import date, timedelta
# from dateutil.relativedelta import relativedelta
#
# from core.models import Task, RecurrenceRule
#
#
# HORIZON_DAYS = 42  # materialise up to 6 weeks ahead
#
#
# # ─── Public API ────────────────────────────────────────────────────────────────
#
# def materialise_instances(template: Task, up_to: date = None) -> list[Task]:
#     """
#     Generate concrete Task instances for `template` up to `up_to`.
#     Skips dates that already have an instance. Returns the created tasks.
#     """
#     _assert_is_template(template)
#
#     if template.due_datetime is None:
#         return []
#
#     up_to = up_to or (date.today() + timedelta(days=HORIZON_DAYS))
#     rule  = template.recurrence_rule
#
#     existing_dates = set(
#         template.instances
#             .exclude(due_datetime=None)
#             .values_list('due_datetime__date', flat=True)
#     )
#
#     new_tasks = [
#         _make_instance(template, occurrence_date)
#         for occurrence_date in _iter_occurrences(rule, start=template.due_datetime.date(), up_to=up_to)
#         if occurrence_date not in existing_dates
#     ]
#
#     return Task.objects.bulk_create(new_tasks)
#
#
# def edit_instance(instance: Task, scope: str) -> None:
#     """
#     Apply scope logic when editing an instance.
#
#     Mutates the template's rule in-place before calling this — this function
#     only handles deleting the relevant existing instances so materialise_instances
#     can regenerate them cleanly.
#
#       'this'   — detach this instance from the series (no rule changes needed).
#       'future' — delete this instance and all future ones.
#       'all'    — delete every incomplete instance.
#     """
#     _assert_is_instance(instance)
#     template = instance.recurrence_source
#
#     if scope == 'this':
#         instance.recurrence_source = None
#         instance.save(update_fields=['recurrence_source'])
#
#     elif scope == 'future':
#         template.instances.filter(
#             due_datetime__date__gte=instance.due_datetime.date()
#         ).delete()
#
#     elif scope == 'all':
#         template.instances.filter(
#             status=Task.Status.TO_DO
#         ).delete()
#
#     else:
#         raise ValueError(f"Unknown scope '{scope}'. Expected 'this', 'future', or 'all'.")
#
#
# def remove_recurrence(template: Task) -> None:
#     """
#     Strip recurrence from a template task entirely.
#     Deletes all instances and the RecurrenceRule row.
#     """
#     _assert_is_template(template)
#
#     template.instances.all().delete()
#     rule = template.recurrence_rule
#     template.recurrence_rule = None
#     template.save(update_fields=['recurrence_rule'])
#     rule.delete()
#
#
# # ─── Internal helpers ──────────────────────────────────────────────────────────
#
# def _iter_occurrences(rule: RecurrenceRule, start: date, up_to: date):
#     """Yield occurrence dates from `start` up to and including `up_to`."""
#     cursor = start
#
#     while cursor <= up_to:
#         if rule.end_date and cursor > rule.end_date:
#             break
#
#         yield cursor
#
#         if rule.frequency == RecurrenceRule.Frequency.DAILY:
#             cursor += timedelta(days=rule.interval)
#         elif rule.frequency == RecurrenceRule.Frequency.WEEKLY:
#             cursor += timedelta(weeks=rule.interval)
#         elif rule.frequency == RecurrenceRule.Frequency.MONTHLY:
#             cursor += relativedelta(months=rule.interval)
#         else:
#             raise ValueError(f"Unhandled frequency '{rule.frequency}'.")
#
#
# def _make_instance(template: Task, due_date: date) -> Task:
#     """Build (but don't save) a Task instance for a given date."""
#     return Task(
#         project           = template.project,
#         parent_task       = template.parent_task,
#         name              = template.name,
#         description       = template.description,
#         status            = Task.Status.TO_DO,
#         recurrence_source = template,
#         due_datetime      = template.due_datetime.replace(
#             year=due_date.year,
#             month=due_date.month,
#             day=due_date.day,
#         ),
#     )
#
#
# def _assert_is_template(task: Task) -> None:
#     if task.recurrence_rule_id is None:
#         raise ValueError(f"Task {task.id} has no recurrence_rule — it is not a template.")
#
#
# def _assert_is_instance(task: Task) -> None:
#     if task.recurrence_source_id is None:
#         raise ValueError(f"Task {task.id} has no recurrence_source — it is not an instance.")