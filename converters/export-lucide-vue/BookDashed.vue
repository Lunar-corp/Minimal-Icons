<template>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    :width="size"
    :height="size"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    :stroke-width="stroke"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path d="M20 22h-2" />
    <path d="M20 15v2h-2" />
    <path d="M4 19.5V15" />
    <path d="M20 8v3" />
    <path d="M18 2h2v2" />
    <path d="M4 11V9" />
    <path d="M12 2h2" />
    <path d="M12 22h2" />
    <path d="M12 17h2" />
    <path d="M8 22H6.5a2.5 2.5 0 0 1 0-5H8" />
    <path d="M4 5v-.5A2.5 2.5 0 0 1 6.5 2H8" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>