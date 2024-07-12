from django.utils import timezone
from .models import Services

class ServicesQueryManager:
    @staticmethod
    def get_all_services(cat_name=None, username=None, tag_name=None):
        """
        Retrieves all services that are currently active and optionally filtered by category, author, or tag.
        """
        current_time = timezone.now()
        query = """
            SELECT *
            FROM services_services
            WHERE status = TRUE AND published_date <= %s
        """
        params = [current_time]

        if cat_name:
            query += " AND category_id IN (SELECT id FROM services_category WHERE name = %s)"
            params.append(cat_name)

        if username:
            query += " AND author_id IN (SELECT id FROM auth_user WHERE username = %s)"
            params.append(username)

        if tag_name:
            query += """
                AND id IN (
                    SELECT service_id
                    FROM services_services_tags
                    INNER JOIN services_tag ON services_services_tags.tag_id = services_tag.id
                    WHERE services_tag.name = %s
                )
            """
            params.append(tag_name)

        query += " ORDER BY published_date DESC"

        return Services.objects.raw(query, params)

    @staticmethod
    def search_services(query):
        """
        Searches for services where the title or content matches the query string.
        """
        sql_query = """
            SELECT *
            FROM services_services
            WHERE status = TRUE AND (title LIKE %s OR content LIKE %s)
            ORDER BY published_date DESC
        """
        params = [f'%{query}%', f'%{query}%']

        return Services.objects.raw(sql_query, params)
