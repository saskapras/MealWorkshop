# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: MealWorkshop
def bulk_delete_records(self, table_name: str) -> int:
        """Delete all records from a given table if confirmation is enabled."""
        if not getattr(self, '_bulk_delete_enabled', False):
            raise PermissionError("Bulk deletion disabled. Set _bulk_delete_enabled = True to allow.")
        count = self._execute_sql(f"DELETE FROM {table_name}", fetch=False)
        return count
