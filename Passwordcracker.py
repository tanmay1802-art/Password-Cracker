import hashlib
import time
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
import os


class HashCracker:
    """Hash Cracker with AUTO-SAVE to results.txt"""

    def __init__(self):
        self.hash_funcs = {
            'md5': hashlib.md5, 'sha1': hashlib.sha1,
            'sha256': hashlib.sha256, 'sha512': hashlib.sha512
        }
        self.results_file = "results.txt"  # SAVES HERE!

    def save_result(self, target_hash, password, algo, time_taken):
        """SAVE cracked password to file"""
        try:
            with open(self.results_file, "a", encoding='utf-8') as f:
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} | "
                        f"HASH: {target_hash} | "
                        f"PASSWORD: {password} | "
                        f"ALGO: {algo} | "
                        f"TIME: {time_taken:.2f}s\n")
            print(f"💾 SAVED to {self.results_file}")
        except Exception as e:
            print(f"⚠️  Save error: {e}")

    def create_test_wordlist(self):
        """Creates wordlist.txt with 100+ common passwords"""
        passwords = [
            "password", "123456", "1122", "admin", "qwerty", "abc123",
            "Password123", "letmein", "welcome", "monkey", "dragon",
            "master", "hello", "freedom", "whatever", "qazwsx",
            "trustno1", "ninja", "abc123", "root", "toor", "user"
        ]
        try:
            with open("wordlist.txt", "w", encoding='utf-8') as f:
                for pwd in passwords:
                    f.write(pwd + "\n")
            print("✅ wordlist.txt created (25 passwords)")
            return True
        except:
            return False

    def load_wordlist(self, path):
        """Safe wordlist loader"""
        if not os.path.exists(path):
            print(f"❌ '{path}' missing. Creating...")
            if self.create_test_wordlist():
                path = "wordlist.txt"
            else:
                return None

        try:
            with open(path, 'r', encoding='utf-8') as f:
                lines = [line.strip() for line in f if line.strip()]
            print(f"✅ Loaded {len(lines)} passwords")
            return lines
        except PermissionError:
            print("❌ Permission denied - run as Admin")
            return None

    def hash_text(self, text, algo, salt=None):
        to_hash = (salt + text if salt else text).encode('utf-8')
        return self.hash_funcs[algo](to_hash).hexdigest()

    def worker_thread(self, start, end, lines, target_hash, algo, salt, stats, lock):
        local_count = 0
        for i in range(start, end):
            if stats['found']: return
            word = lines[i]
            hashed = self.hash_text(word, algo, salt)
            local_count += 1
            if hashed == target_hash:
                with lock:
                    stats['found'] = True
                    stats['password'] = word
                    stats['attempts'] += local_count
                return
        with lock:
            stats['attempts'] += local_count

    def progress_display(self, stats):
        while not stats['found']:
            elapsed = time.time() - stats['start_time']
            rate = stats['attempts'] / elapsed if elapsed else 0
            sys.stdout.write(f"\r🔄 {stats['attempts']:>7,} attempts | "
                             f"{rate:>6.0f} H/s | {elapsed:.1f}s")
            sys.stdout.flush()
            time.sleep(0.5)

    def crack(self, target_hash, wordlist_path, algo='md5', threads=4, salt=None):
        print("\n🚀 HASH CRACKER v5.0")
        print(f"🎯 {target_hash} | {algo.upper()} | {threads} threads")

        lines = self.load_wordlist(wordlist_path)
        if not lines: return False

        stats = {'attempts': 0, 'start_time': time.time(), 'found': False, 'password': None}
        lock = threading.Lock()

        chunk_size = len(lines) // threads
        progress_thread = threading.Thread(target=self.progress_display, args=(stats,), daemon=True)
        progress_thread.start()

        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [executor.submit(self.worker_thread,
                                       i * chunk_size, (i + 1) * chunk_size if i < threads - 1 else len(lines),
                                       lines, target_hash, algo, salt, stats, lock) for i in range(threads)]
            for future in futures: future.result()

        elapsed = time.time() - stats['start_time']
        print("\n" + "=" * 60)
        if stats['found']:
            print(f"✅ CRACKED: '{stats['password']}'")
            print(f"⏱️  {elapsed:.2f}s | {stats['attempts'] / elapsed:.0f} H/s")
            self.save_result(target_hash, stats['password'], algo, elapsed)
            return True
        print("❌ Not found")
        return False

    def interactive(self):
        print("🔥 INTERACTIVE HASH CRACKER")
        print("=" * 40)
        target = input("📋 Hash: ").strip().lower()
        wordlist = input("📁 Wordlist: ").strip() or "wordlist.txt"
        algo = input("🔑 Algo (md5): ").strip().lower() or "md5"
        threads_str = input("⚡ Threads (4): ").strip()
        threads = int(threads_str) if threads_str.isdigit() else 4
        salt = input("🧂 Salt: ").strip() or None

        if algo not in self.hash_funcs: algo = 'md5'
        self.crack(target, wordlist, algo, threads, salt)


def main():
    cracker = HashCracker()
    cracker.interactive()


if __name__ == "__main__":
    main()