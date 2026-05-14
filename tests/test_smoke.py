"""Смоук-тесты репозитория (без клона курса distrib_systems_tasks)."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_docker_compose_file_exists():
    assert (ROOT / "docker-compose.yml").is_file()


def test_gateway_stack_files():
    assert (ROOT / "infra" / "nginx.conf").is_file()
    assert (ROOT / "services" / "events" / "main.py").is_file()
    assert (ROOT / "services" / "other" / "main.py").is_file()


def test_lab10_docker_context():
    d = ROOT / "labs" / "week-10"
    assert (d / "Dockerfile").is_file()
    assert (d / "app" / "main.py").is_file()
    assert (d / "requirements.txt").is_file()


def test_k8s_yaml_parse():
    dep = ROOT / "labs" / "week-12" / "k8s" / "deployment.yaml"
    svc = ROOT / "labs" / "week-12" / "k8s" / "service.yaml"
    assert yaml.safe_load(dep.read_text(encoding="utf-8"))["kind"] == "Deployment"
    assert yaml.safe_load(svc.read_text(encoding="utf-8"))["kind"] == "Service"


def test_saga_next_state():
    import importlib.util

    saga = ROOT / "labs" / "week-04" / "app" / "saga.py"
    spec = importlib.util.spec_from_file_location("saga", saga)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert mod.next_state("NEW", "PAY_OK") == "PAID"
    assert mod.next_state("NEW", "PAY_FAIL") == "CANCELLED"
