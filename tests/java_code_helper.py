import os
import glob
import shutil
import subprocess
import tempfile


def find_javac():
    javac = shutil.which("javac")
    if javac:
        return javac
    for pattern in (
        r"C:\Program Files\Eclipse Adoptium\*\bin\javac.exe",
        r"C:\Program Files\Java\*\bin\javac.exe",
        r"C:\Program Files\Microsoft\jdk-*\bin\javac.exe",
    ):
        hits = glob.glob(pattern)
        if hits:
            return sorted(hits)[-1]
    return None


JAVAC = find_javac()


def compile_java(results):
    """
    Writes the emitted java_code files to a temp dir and compiles them together with javac.
    Returns (ok, output). ok is None when javac is not installed (caller should skip).
    """
    if JAVAC is None:
        return None, "javac not found"

    with tempfile.TemporaryDirectory() as work:
        files = []
        for code in results:
            path = os.path.join(work, code.fileName)  # javac reads the package from the source
            with open(path, "w") as f:
                f.write(code.content)
            files.append(path)

        out = os.path.join(work, "_out")
        os.makedirs(out, exist_ok=True)
        proc = subprocess.run([JAVAC, "-d", out] + files, capture_output=True, text=True)
        return proc.returncode == 0, proc.stdout + proc.stderr
