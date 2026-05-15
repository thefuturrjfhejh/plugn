from pathlib import Path


view = Path("frontend/views/order/view.php").read_text()

required_snippets = [
    "$providerTrackingLink = static function ($value) use ($encodeProviderValue)",
    "filter_var($value, FILTER_VALIDATE_URL)",
    "Html::a(Html::encode($value), $value, [",
    "'rel' => 'noopener noreferrer'",
    "$providerStatusBadge = static function ($value)",
    "Html::encode($value)",
    "return $providerTrackingLink($data->armada_tracking_link);",
    "return $providerTrackingLink($data->mashkor_tracking_link);",
    "return $encodeProviderValue($data->armada_delivery_code);",
    "return $providerStatusBadge($data->armada_order_status);",
    "return $encodeProviderValue($data->mashkor_order_number);",
    "return $encodeProviderValue($data->mashkor_driver_phone);",
    "return $encodeProviderValue($data->mashkor_driver_name);",
]

for snippet in required_snippets:
    if snippet not in view:
        raise SystemExit(f"Missing frontend order provider escaping guard: {snippet}")

forbidden_snippets = [
    "Html::a($data->armada_tracking_link",
    "Html::a($data->armada_delivery_code",
    "Html::a($data->mashkor_tracking_link",
    "\\yii\\helpers\\Url::to($data->armada_tracking_link",
    "\\yii\\helpers\\Url::to($data->armada_delivery_code",
    "\\yii\\helpers\\Url::to($data->mashkor_tracking_link",
    "' . $data->armada_order_status . '",
    "return $data->mashkor_order_number ? $data->mashkor_order_number : null;",
    "return $data->mashkor_driver_phone ? $data->mashkor_driver_phone : null;",
    "return $data->mashkor_driver_name ? $data->mashkor_driver_name : null;",
]

for snippet in forbidden_snippets:
    if snippet in view:
        raise SystemExit(f"Unsafe frontend order provider rendering remains: {snippet}")

print("frontend order provider fields are escaped")
