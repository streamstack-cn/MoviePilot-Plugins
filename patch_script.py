import os

patch_code = """
# === P115Client / concurrenttools Compatibility Patch ===
try:
    import concurrenttools
    if not hasattr(concurrenttools, 'threadpool_map') and hasattr(concurrenttools, 'thread_conmap'):
        concurrenttools.threadpool_map = concurrenttools.thread_conmap
    if not hasattr(concurrenttools, 'taskgroup_map') and hasattr(concurrenttools, 'async_conmap'):
        concurrenttools.taskgroup_map = concurrenttools.async_conmap
except ImportError:
    pass
# ========================================================
"""

def apply_patch(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    if "Compatibility Patch" in content:
        return
        
    with open(filepath, 'w') as f:
        f.write(patch_code + "\n" + content)

apply_patch("plugins.v2/p115strmhelper/__init__.py")
apply_patch("plugins.v2/p115disk/__init__.py")
print("Patch applied successfully.")
