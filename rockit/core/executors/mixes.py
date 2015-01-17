
import time

class MixesExecutor(object):

    IDENTIFIER_ALARM    = 'when-alarm'
    IDENTIFIER_BUTTON   = 'when-button'
    IDENTIFIER_SCHEDULE = 'when-schedule'

    IDENTIFIER_MAILOUT  = 'finish-mailout'

    def __init__(self):
        self.details = {
            self.IDENTIFIER_ALARM: lambda h: self._set_when_alarm_details(h),
            self.IDENTIFIER_BUTTON: lambda h: self._set_when_button_details(h),
            self.IDENTIFIER_SCHEDULE: lambda h: self._set_when_schedule_details(h)
        }

        self.validation = {
            'rockit-alarm': lambda c,h: self._validate_alarm_criteria(c,h)
        }

    def collect(self, holder):
        """
        Collect capabilities of this executor
        """
        for c in self._get_when_capabilities():
            holder.add_when(**c)

        for f in self._get_finish_capabilities():
            holder.add_finish(**f)

        return holder

    def collect_details(self, identifier, holder):
        """
        Collect details about specific mixes
        """
        assert identifier is not None
        assert holder is not None

        if identifier in self.details:
            self.details[identifier](holder)

        return holder

    def validate(self, criterias, validation):

        for criteria in criterias:
            if criteria['id'] in self.validation:
                self.validation[criteria['id']](criteria, validation)

        return validation

    def _add_capabilities(self, container, identifier, name):
        container.append({
            'identifier': identifier,
            'name': name
            })

    def _generate_post(self, identifier, typed, label, required=False, max_length=None):

        data = {
            'identifier': identifier,
            'type': typed,
            'label': label,
            'required': required
        }

        if max_length:
            data['max_length'] = max_length

        return data

    def _get_when_capabilities(self):
        result = list()

        #self._add_capabilities(result, self.IDENTIFIER_BUTTON, 'Button')
        self._add_capabilities(result, self.IDENTIFIER_SCHEDULE, 'Schedule')
        self._add_capabilities(result, self.IDENTIFIER_ALARM, 'Alarm')

        return result

    def _get_finish_capabilities(self):
        result = list()

        self._add_capabilities(result, self.IDENTIFIER_MAILOUT, 'mailout')

        return result

    def is_time_format(self, input):
        try:
            time.strptime(input, '%H:%M')
            return True
        except ValueError:
            return False

    def _set_when_button_details(self, holder):
        holder.add_post(**self._generate_post('name', 'string', 'name', True, 100))

    def _set_when_schedule_details(self, holder):
        holder.add_post(**self._generate_post('rockit-schedule', 'schedule', 'schedule', True))

    def _set_when_alarm_details(self, holder):
        holder.add_post(**self._generate_post('rockit-alarm', 'alarm', 'alarm', True))

    def _validate_alarm_criteria(self, criteria, holder):

        if not self.is_time_format(criteria['value']):
            holder.add_error(criteria['id'], 'Criteria value does not have a time format')

